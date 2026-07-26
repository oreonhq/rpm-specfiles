%global source0_hash 9908689361e263bf198e6acfb3c4386759fb7df7d141f4384d7414771c68d7fc

Name:           stomppy
Version:        8.2.0
Release:        %autorelease
Summary:        Python stomp client for messaging

License:        Apache-2.0
URL:            https://github.com/jasonrbriggs/stomp.py
Source0:        %{pypi_source stomp_py}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

%package -n python3-stomppy
Summary:        Python stomp client for messaging for python3

%description -n python3-stomppy
stomp.py is a Python client library for accessing messaging servers 
(such as ActiveMQ or JBoss Messaging) using the STOMP protocol. It can also
be run as a standalone, command-line client for testing.

This module is for the python3.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n stomp_py-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files stomp

%check
# Upsteream tests require a running activemq, rabbitmq, ....
%pyproject_check_import

%files -n python3-stomppy -f %{pyproject_files}
%{_bindir}/stomp

%changelog
%autochangelog
