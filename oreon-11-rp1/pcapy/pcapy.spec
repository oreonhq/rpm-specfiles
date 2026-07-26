%global source0_hash 2ff96eb65caee8a45a3ae3edb78d5b4d8debcace9dc2921aefa3be83bb0af9c6

%global         gituser         CoreSecurity
%global         gitname         pcapy
%global         commit          b91a418374d1636408c435f11799ef725ef70097
%global         commitdate      20170116

%global         shortcommit     %(c=%{commit}; echo ${c:0:7})
%global         sum             A Python interface to libpcap

%global         with_tests      0

Name:           pcapy
Version:        0.11.5
Release:        29%{?dist}
Summary:        %{sum}

License:        Apache-1.1
URL:            https://www.coresecurity.com/corelabs-research/open-source-tools/pcapy
#               http://oss.coresecurity.com/projects/pcapy.html
#               https://github.com/CoreSecurity/pcapy/releases
#Source0:       https://github.com/%%{gituser}/%%{gitname}/archive/%%{commit}/%%{name}-%%{version}-%%{shortcommit}.tar.gz
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{version}.tar.gz#/%{gitname}-%{version}.tar.gz

# Fix FTBFS issue with setuptools >= 61.0.0
# Upstream issue: https://github.com/helpsystems/pcapy/issues/73
# Fix backported from the fork: https://github.com/stamparm/pcapy-ng/commit/84a15d2faefaae410198f5739d6ed3c69daa17ec
Patch0:         fix-setuptools-build.patch
Patch1:         py_ssize_t.patch
Patch2:         py313.patch

BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  libpcap-devel

%description
Pcapy is a Python extension module that interfaces with the libpcap
packet capture library. Pcapy enables python scripts to capture packets
on the network. Pcapy is highly effective when used in conjunction with 
a packet-handling package such as Impacket, which is a collection of 
Python classes for constructing and dissecting network packets.

#===== the python3 package definition
%package -n python3-%{gitname}
Summary:        %{sum}

%description -n python3-%{gitname}
Python3 package of %{gitname}.
Pcapy is a Python extension module that interfaces with the libpcap
packet capture library. Pcapy enables python scripts to capture packets
on the network. Pcapy is highly effective when used in conjunction with
a packet-handling package such as Impacket, which is a collection of
Python classes for constructing and dissecting network packets.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p0

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

#fix encodings
sed -i 's/\r//' LICENSE
sed -i 's/\r//' README
sed -i 's/\r//' pcapy.html
iconv -f IBM850 -t UTF8 pcapy.html > pcapy.html.tmp
mv pcapy.html.tmp pcapy.html

%install
%pyproject_install
%pyproject_save_files -l '*'

rm -rf %{buildroot}/usr/share/doc/pcapy

%check
%pyproject_check_import

%files -n python3-%{gitname} -f %{pyproject_files}
%doc README pcapy.html

%changelog
%autochangelog
