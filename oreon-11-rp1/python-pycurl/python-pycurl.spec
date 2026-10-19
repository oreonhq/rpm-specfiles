%global source0_hash b70961a76c412cd34f9cc2c9558e63f89fb37045c59eee396c585b52973be280
Name:           python-pycurl
Version:        7.48.0
Release:        1%{?dist}
Summary:        PycURL -- A Python Interface To The cURL library
License:        LGPL-2.1-only OR MIT
URL:            https://pycurl.github.io/
Source0:        https://files.pythonhosted.org/packages/source/p/pycurl/pycurl-%{version}.tar.gz
Patch1:         0001-python-pycurl-7.45.1-tls-backend.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools) >= 77
Requires:       python3-pycurl = %{version}-%{release}
# /oreon:deps
%description

%package -n     python3-pycurl
Summary:        PycURL -- A Python Interface To The cURL library
%description -n python3-pycurl

%prep
%global oreon_srcdir pycurl-%{version}
%oreon_prep
%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-pycurl usr/lib/python3*/site-packages/pycurl* usr/lib64/python3*/site-packages/pycurl* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/pycurl* usr/lib64/python3*/site-packages/pycurl* usr/bin/*

%check

%_pyproject_check_import_allow_no_modules -t
%files
%files -n python3-pycurl -f %{oreon_filedir}/python3-pycurl.list

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
