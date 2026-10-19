%global source0_hash 89587d1b836a5220d74848c934757962b382886dca8b1b4a0c44d693f2600643
Name:           python-impacket
Summary:        Collection of Python classes providing access to network packets
Version:        0_13_1
License:        Apache-1.1 AND Zlib
URL:            https://github.com/fortra/impacket
%global __requires_exclude ldapdomaindump|flask|httplib2
%global         sum             Collection of Python classes providing access to network packets
%global         common_desc     %{expand:
Impacket is a collection of Python classes focused on providing access to
network packets. Impacket allows Python developers to craft and decode network
packets in simple and consistent manner. It is highly effective when used in
conjunction with a packet capture utility or package such as Pcapy. Packets
can be constructed from scratch, as well as parsed from raw data. Furthermore,
the object oriented API makes it simple to work with deep protocol hierarchies.}
%global __requires_exclude ldapdomaindump|flask|httplib2|dsinternals
%global         gituser         fortra
%global         gitname         impacket
%global         commit          5af85c240076444d631d5f504e294daff065796b
%global         gitdate         20230731
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%bcond_without  python3
%global         pkgver          %(echo %{version} | sed 's/\\./_/g')
%bcond_without  release
%if %{with release}
Release:        1%{?dist}
Source0:        https://github.com/%{gituser}/%{gitname}/releases/download/%{gitname}_%{version}/%{gitname}-%{version}.tar.gz
%else
Release:        1%{?dist}
%endif
Patch0:         python-impacket-0.12.0-cleanup.patch
Patch1:         python-impacket-0.12.0-pyopenssl.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  grep
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sed
# /oreon:deps
%description
%{common_desc}

#===== the python3 package definition
%package -n python%{python3_pkgversion}-%{gitname}
Summary:        %{sum}
%{?python_provide:%python_provide python%{python3_pkgversion}-%{gitname}}
Provides:       impacket = %{version}-%{release}
Requires:       python%{python3_pkgversion}-pycryptodomex
Requires:       python%{python3_pkgversion}-pyasn1
Requires:       python%{python3_pkgversion}-pyOpenSSL
Requires:       python%{python3_pkgversion}-ldap3
%global __requires_exclude pcapy|ldapdomaindump|flask|httplib2
Requires:       python%{python3_pkgversion}-httplib2
Requires:       python%{python3_pkgversion}-flask
%description -n python%{python3_pkgversion}-%{gitname}
Python3 package of %{name}. %{common_desc}

#===== Preparation
%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%if %{with release}
# Build from git release version
%autosetup -p 1 -n %{gitname}-%{version}

# https://github.com/fortra/impacket/pull/1689
# 1) set library modules as non-executable as there is no main functionality and is meant to be used only via import
# impacket/examples/ldap_shell.py
# impacket/examples/smbclient.py
# 2) convert ends of lines from windows to unix (as rest of the project) for the file impacket/examples/mssqlshell.py
# 3) remove unnecessary shebang for impacket/examples/mssqlshell.py
chmod -x impacket/examples/ldap_shell.py impacket/examples/smbclient.py
sed -i -e 's/\r//g' impacket/examples/mssqlshell.py

%else
# Build from git commit
%autosetup -p 1 -n %{gitname}-%{commit}
%endif

# Clean-up

# Use explicit python3 shabeng instead of generic env python
%py3_shebang_fix impacket examples

# Rename split.py to splitpcap.py due to generic name colliding with DiderStevensSuite
# https://github.com/fortra/impacket/issues/1938
mv examples/split.py examples/splitpcap.py
sed -i -e "s%/split.py%/splitpcap.py%" impacket.egg-info/SOURCES.txt

# Drop useles dependency on future
# https://github.com/fortra/impacket/commit/d7b5e3 - will be fixed in 0_13_1
sed -i "s/'future',//" setup.py

#===== Build
%build

%py3_build
%check

PYTHONPATH=$BUILD_ROOT/usr/lib/python%{python3_version}/site-packages/ python3 -c \
    'import impacket.ImpactPacket ; impacket.ImpactPacket.IP().get_packet()'
%install
%py3_install
rm -f %{buildroot}%{_defaultdocdir}/%{name}/LICENSE
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%if %{with python3}
%files -f %{oreon_filedir}/main.list
%files -n python3-impacket -f %{oreon_filedir}/python3-impacket.list

%changelog

%autochangelog
%endif
