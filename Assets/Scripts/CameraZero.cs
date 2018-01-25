using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CameraZero : MonoBehaviour {

    public CubeBehavior getFlag;
    bool value;
    
    // Use this for initialization
	void Start () {
        getFlag = getFlag.GetComponent<CubeBehavior>();
        value = true;
        this.gameObject.transform.rotation = Quaternion.identity;
    }
	
	// Update is called once per frame
	void Update () {
        if (!getFlag.flag && value)
        {
            this.gameObject.transform.rotation = Quaternion.identity;
            value = false;
        }
        else
            return;
	}
}
