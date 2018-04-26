package com.uncleheart.utils.System;

import android.Manifest;
import android.app.Activity;
import android.content.pm.PackageManager;
import android.os.Build;

/**
 * Created by uncleheart on 2018/4/26.
 */

public class Permission {
    public static Permission instance;

    public static synchronized Permission getInstance() {
        if (instance == null)
            instance = new Permission();
        return instance;
    }

    /**
     * 请求外部存储的读写权限，要求以及在AndroidManifest.xml已注册权限
     * <uses-permission android:name="android.permission.INTERNET" />
     * <uses-permission android:name="android.permission.INTERNET" />
     * @param activity
     * @return
     */
    public boolean isGrantExternalRW(Activity activity) {
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M && activity.checkSelfPermission(
                Manifest.permission.WRITE_EXTERNAL_STORAGE) != PackageManager.PERMISSION_GRANTED) {

            activity.requestPermissions(new String[]{
                    Manifest.permission.READ_EXTERNAL_STORAGE,
                    Manifest.permission.WRITE_EXTERNAL_STORAGE
            }, 1);

            return false;
        }

        return true;
    }
}
