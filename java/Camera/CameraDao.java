package com.gmi.its.itsmain.dao;

import java.util.List;

import org.apache.ibatis.annotations.Param;
import org.springframework.stereotype.Repository;

import com.gmi.its.itsmain.model.Camera;

@Repository
public interface CameraDao {
	void insertCamera(Camera camera);
	void updateCamera(@Param("item")Camera camera);
	void deleteCamera(String uniqueNums[]);
	List<Camera> selectCamera(@Param("deviceId")String deviceId);
}