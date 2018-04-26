package com.uncleheart.utils.System;//在任意位置获取context

import android.app.Application;
import android.content.Context;

public class NormalConfig {


    public static NormalConfig instance;

    public static synchronized NormalConfig getInstance() {
        if (instance == null)
            instance = new NormalConfig();
        return instance;
    }

    private static Context context = null;

    /**
     * 获取context，另外一种思路就是添加Application类，然后存储context值即可
     * @return 返回当前的Context
     */
    public  Context getContext() {
        if(context==null) {

            try {
                Application application = (Application) Class.forName("android.app.ActivityThread").getMethod("currentApplication").invoke(null, (Object[]) null);
                context = application.getApplicationContext();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return context;
    }

    /**
     * 另外一种方法获取context
     * @return 返回当前的Context
     */
    public  Context getContext_() {
        if(context==null) {
            try {
                Application application = (Application) Class.forName("android.app.AppGlobals").getMethod("getInitialApplication").invoke(null, (Object[]) null);
                context = application.getApplicationContext();

            } catch (Exception e) {
                e.printStackTrace();
            }
        }
        return context;
    }
}