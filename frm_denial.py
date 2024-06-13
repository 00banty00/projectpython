if flag_day1 == 'N' and flag_active == 'Y':
        print("***INSIDE INCREMENTAL LOAD***")
        hcp_omni_denial_trends_df = prepare_frm_denial_trends_daily(frm_denial_trends_weekly_df, iqvia_alerts_config_df)
        hcp_omni_denial_trends_df.show(5)
        col_list_denial_trends = hcp_omni_denial_trends_df.columns

        # Reading Snapshot data
        hcp_omni_denial_trends_snap_df = input_data.read_hcp_omni_frm_denial_trends_weekly(spark, norm_hcp_bucket_snap_path)

        hcp_omni_denial_trends_snap_df = hcp_omni_denial_trends_snap_df.select(sorted(col_list_denial_trends))
        hcp_omni_denial_trends_df = hcp_omni_denial_trends_df.select(sorted(col_list_denial_trends))

        hcp_omni_denial_trends_df.printSchema()
        hcp_omni_denial_trends_snap_df.printSchema()

        # Combining latest and history data
        hcp_omni_denial_trends_final_df = hcp_omni_denial_trends_df.unionAll(hcp_omni_denial_trends_snap_df) \
                                                                                .select(*col_list_denial_trends)
        write_to_s3(hcp_omni_denial_trends_final_df, norm_hcp_bucket_path)