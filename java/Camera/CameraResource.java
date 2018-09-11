package com.gmi.its.itsmain.resources;

import java.util.List;
import javax.ws.rs.DELETE;
import javax.ws.rs.GET;
import javax.ws.rs.POST;
import javax.ws.rs.PUT;
import javax.ws.rs.Path;
import javax.ws.rs.Produces;
import javax.ws.rs.QueryParam;
import javax.ws.rs.core.GenericEntity;
import javax.ws.rs.core.Response;
import javax.ws.rs.core.Response.Status;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

import com.gmi.its.itsmain.model.Camera;
import com.gmi.its.itsmain.service.CameraService;

@Path("camera")
@Produces("application/json;charset=utf-8")
@Component
public class CameraResource {
	@Autowired
	private CameraService cameraService;

	@POST
	@Path("/Camera")
	public Response insertCamera(Camera camera) {
		try {
			cameraService.insertCamera(camera);
			return Response.status(Status.OK).entity("SUCCESS").build();
		} catch (Exception e) {
			return Response.status(Status.BAD_REQUEST).entity("ERROR").build();
		}
	}

	@PUT
	@Path("/Camera")
	public Response updateCamera(Camera camera) {
		try {
			cameraService.updateCamera(camera);
			return Response.status(Status.OK).entity("SUCCESS").build();
		} catch (Exception e) {
			return Response.status(Status.BAD_REQUEST).entity("ERROR").build();
		}
	}

	@DELETE
	@Path("/Camera")
	public Response deleteCamera(@QueryParam("deviceId") String deviceId) {
		try {
			String[] cameras = deviceId.split(",");
			cameraService.deleteCamera(cameras);
			return Response.status(Status.OK).entity("SUCCESS").build();
		} catch (Exception e) {
			return Response.status(Status.BAD_REQUEST).entity("ERROR").build();
		}
	}

	@GET
	@Path("/Camera")
	public Response selectCamera(@QueryParam("deviceId") String deviceId) {
		try {
			List<Camera> camera = cameraService.selectCamera(deviceId);GenericEntity<List<Camera>> entity = new GenericEntity<List<Camera>>(camera) {};
			return Response.status(Status.OK).entity(entity).build();
		} catch (Exception e) {
			return Response.status(Status.BAD_REQUEST).entity("ERROR").build();
		}
	}
}