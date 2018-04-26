package com.uncleheart.utils.System;

import android.util.Log;

/**
 * Created by uncleheart on 2018/4/26.
 */

public class LogPlus {
    public static LogPlus instance;

    public static synchronized LogPlus getInstance() {
        if (instance == null)
            instance = new LogPlus();
        return instance;
    }

    public static String TAG = "changerlog";

    public void logInfo(String str, Object... args) {
        logInfo(null, str, args);
    }

    public void logInfo(Throwable e, String str, Object... args) {
        String logStr = String.format(str, args);
        Log.i(TAG, logStr, e);
    }

    public void logDebug(String str, Object... args) {
        logDebug(null, str, args);
    }

    public void logDebug(Throwable e, String str, Object... args) {
        String logStr = String.format(str, args);
        Log.d(TAG, logStr, e);
    }

    public void logWarring(String str, Object... args) {
        logWarring(null, str, args);
    }

    public void logWarring(Throwable e, String str, Object... args) {
        String logStr = String.format(str, args);
        Log.w(TAG, logStr, e);
    }

    public void logError(String str, Object... args) {
        logError(null, str, args);
    }

    public void logError(Throwable e, String str, Object... args) {
        String logStr = String.format(str, args);
        Log.e(TAG, logStr, e);
    }

}
