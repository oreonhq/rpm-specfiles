%global source0_hash b70961a76c412cd34f9cc2c9558e63f89fb37045c59eee396c585b52973be280

Name:           python-pycurl
Version:        7.48.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        PycURL -- A Python Interface To The cURL library

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        LGPL-2.1-only OR MIT
URL:            https://pycurl.github.io/
Source:         %{pypi_source pycurl}

BuildRequires:  libcurl-devel
BuildRequires:  python3-devel
BuildRequires:  gcc


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'pycurl' generated automatically by pyp2spec.}

Patch1:         0001-python-pycurl-7.45.1-tls-backend.patch

%description %_description

%package -n     python3-pycurl
Summary:        %{summary}

%description -n python3-pycurl %_description


%prep
%autosetup -p1 -n pycurl-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-pycurl -f %{pyproject_files}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.45.7-2
- Prepare for Oreon 11 (RP1)
/usr/share/doc/pycurl/examples/__pycache__/async_multi.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/basicfirst.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/file_upload.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/multi-socket_action-select.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/opensocketexception.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/retriever-multi.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/retriever.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/sfquery.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/smtp.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/ssh_keyfunction.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/ws_callback.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/ws_echo.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/ws_fragmented.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/ws_multi.cpython-314.pyc
/usr/share/doc/pycurl/examples/__pycache__/xmlrpc_curl.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_buffer.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_real.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/file_upload_real_fancy.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/follow_redirect.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/form_post.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/get.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/put_buffer.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/put_file.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/response_headers.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/response_info.cpython-314.pyc
/usr/share/doc/pycurl/examples/quickstart/__pycache__/write_file.cpython-314.pyc
/usr/share/doc/pycurl/examples/__p
