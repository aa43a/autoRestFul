package com.gmi.its.itsmain.service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import java.util.List;


import com.gmi.its.itsmain.dao.CameraDao;
import com.gmi.its.itsmain.model.Camera;

@Service
public class CameraServiceImpl implements CameraService {
	@Autowired
	private CameraDao cameraDao;
	@Override
	public void insertCamera(Camera camera){
		cameraDao.insertCamera(camera);
	}
	@Override
	public void updateCamera(Camera camera){
		cameraDao.updateCamera(camera);
	}
	@Override
	public void deleteCamera(String uniqueNums[]){
		cameraDao.deleteCamera(uniqueNums);
	}
	@Override
	public List<Camera> selectCamera(String deviceId){

		return cameraDao.selectCamera(deviceId);
	}
}