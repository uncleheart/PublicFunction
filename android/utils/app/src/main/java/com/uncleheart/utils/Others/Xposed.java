package com.uncleheart.utils.Others;

import com.uncleheart.utils.System.LogPlus;

/**
 * Created by uncleheart on 2018/4/26.
 */

public class Xposed {
    public static Xposed instance;

    public static synchronized Xposed getInstance() {
        if (instance == null)
            instance = new Xposed();
        return instance;
    }

    public boolean isXposedLoad() {
        boolean isPresent = false;
        try {
            isPresent = (null != Class.forName("de.robv.android.xposed.XSharedPreferences"));
        } catch (ClassNotFoundException e) {

        }
        LogPlus.getInstance().logDebug("xposed load? %b", isPresent);
        return isPresent;
    }
}
