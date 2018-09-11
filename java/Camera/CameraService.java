package com.gmi.its.itsmain.service;

import java.util.List;

import com.gmi.its.itsmain.model.Camera;

public interface CameraService {
	public void insertCamera(Camera camera);
	public void updateCamera(Camera camera);
	public void deleteCamera(String uniqueNums[]);
	public List<Camera> selectCamera(String deviceId);
}