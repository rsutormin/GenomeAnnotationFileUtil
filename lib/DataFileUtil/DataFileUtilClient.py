############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport
import time


class DataFileUtil(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login',
            service_ver='release',
            async_job_check_time_ms=5000):
        if url is None:
            url = 'https://kbase.us/services/njs_wrapper'
        self._service_ver = service_ver
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc,
            async_job_check_time_ms=async_job_check_time_ms)

    def _check_job(self, job_id):
        return self._client._check_job('DataFileUtil', job_id)

    def _shock_to_file_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.shock_to_file', [params],
             self._service_ver, context)

    def shock_to_file(self, params, context=None):
        """
        Download a file from Shock.
        :param params: instance of type "ShockToFileParams" (Input for the
           shock_to_file function. Required parameters: shock_id - the ID of
           the Shock node. file_path - the location to save the file output.
           If this is a directory, the file will be named as per the filename
           in Shock. Optional parameters: unpack - if the file is compressed
           and / or a file bundle, it will be decompressed and unbundled into
           the directory containing the original output file. unpack supports
           gzip, bzip2, tar, and zip files. Default false. Currently
           unsupported.) -> structure: parameter "shock_id" of String,
           parameter "file_path" of String, parameter "unpack" of type
           "boolean" (A boolean - 0 for false, 1 for true. @range (0, 1))
        :returns: instance of type "ShockToFileOutput" (Output from the
           shock_to_file function. node_file_name - the filename of the file
           stored in Shock. attributes - the file attributes, if any, stored
           in Shock.) -> structure: parameter "node_file_name" of String,
           parameter "attributes" of mapping from String to unspecified object
        """
        job_id = self._shock_to_file_submit(params, context)
        while True:
            time.sleep(self._client.async_job_check_time)
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _file_to_shock_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.file_to_shock', [params],
             self._service_ver, context)

    def file_to_shock(self, params, context=None):
        """
        Load a file to Shock.
        :param params: instance of type "FileToShockParams" (Input for the
           file_to_shock function. Required parameters: file_path - the
           location of the file to load to Shock. Optional parameters:
           attributes - user-specified attributes to save to the Shock node
           along with the file. make_handle - make a Handle Service handle
           for the shock node. Default false. gzip - gzip the file before
           loading it to Shock. This will create a file_path.gz file prior to
           upload. Default false.) -> structure: parameter "file_path" of
           String, parameter "attributes" of mapping from String to
           unspecified object, parameter "make_handle" of type "boolean" (A
           boolean - 0 for false, 1 for true. @range (0, 1)), parameter
           "gzip" of type "boolean" (A boolean - 0 for false, 1 for true.
           @range (0, 1))
        :returns: instance of type "FileToShockOutput" (Output of the
           file_to_shock function. shock_id - the ID of the new Shock node.
           handle - the new handle, if created. Null otherwise.) ->
           structure: parameter "shock_id" of String, parameter "handle" of
           type "Handle" (A handle for a file stored in Shock. hid - the id
           of the handle in the Handle Service that references this shock
           node id - the id for the shock node url - the url of the shock
           server type - the type of the handle. This should always be
           shock. file_name - the name of the file remote_md5 - the md5
           digest of the file.) -> structure: parameter "hid" of String,
           parameter "file_name" of String, parameter "id" of String,
           parameter "url" of String, parameter "type" of String, parameter
           "remote_md5" of String
        """
        job_id = self._file_to_shock_submit(params, context)
        while True:
            time.sleep(self._client.async_job_check_time)
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _copy_shock_node_submit(self, params, context=None):
        return self._client._submit_job(
             'DataFileUtil.copy_shock_node', [params],
             self._service_ver, context)

    def copy_shock_node(self, params, context=None):
        """
        Copy a Shock node.
        :param params: instance of type "CopyShockNodeParams" (Input for the
           copy_shock_node function. Required parameters: shock_id - the id
           of the node to copy. Optional parameters: make_handle - make a
           Handle Service handle for the shock node. Default false.) ->
           structure: parameter "shock_id" of String, parameter "make_handle"
           of type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1))
        :returns: instance of type "CopyShockNodeOutput" (Output of the
           copy_shock_node function. shock_id - the id of the new Shock node.
           handle - the new handle, if created. Null otherwise.) ->
           structure: parameter "shock_id" of String, parameter "handle" of
           type "Handle" (A handle for a file stored in Shock. hid - the id
           of the handle in the Handle Service that references this shock
           node id - the id for the shock node url - the url of the shock
           server type - the type of the handle. This should always be
           shock. file_name - the name of the file remote_md5 - the md5
           digest of the file.) -> structure: parameter "hid" of String,
           parameter "file_name" of String, parameter "id" of String,
           parameter "url" of String, parameter "type" of String, parameter
           "remote_md5" of String
        """
        job_id = self._copy_shock_node_submit(params, context)
        while True:
            time.sleep(self._client.async_job_check_time)
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result'][0]

    def _versions_submit(self, context=None):
        return self._client._submit_job(
             'DataFileUtil.versions', [],
             self._service_ver, context)

    def versions(self, context=None):
        """
        Get the versions of the Workspace service and Shock service.
        :returns: multiple set - (1) parameter "wsver" of String, (2)
           parameter "shockver" of String
        """
        job_id = self._versions_submit(context)
        while True:
            time.sleep(self._client.async_job_check_time)
            job_state = self._check_job(job_id)
            if job_state['finished']:
                return job_state['result']
