%global source0_hash 34a2eb29c5e59a2138cc4c06f27bc2d41ff7ef7d85f0f6c4ce0c421ba5a2c4d8

%global commit c575ea33f92495b4b0ccdb1ce09099f9c011e43f
%global commitdate 20190613
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           mx5000tools
Version:        0.1.2
Release:        20.%{commitdate}git%{shortcommit}%{?dist}
Summary:        Tools for the MX5000 series keyboard
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://github.com/jwrdegoede/mx5000tools
Source0:        https://github.com/jwrdegoede/mx5000tools/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source1:        90-mx5000tools.rules
BuildRequires: make
BuildRequires:  gcc netpbm-devel libtool systemd-rpm-macros
Provides:       %{name}-libs = %{version}-%{release}
Obsoletes:      %{name}-libs < %{version}-%{release}
# for _udevrulesdir ownership
Requires:       systemd-udev

%description
mx5000tools are tools to control the extra features on the Logitech MX
5000 Bluetooth cordless keyboard. 

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit}
autoreconf -ivf

%build
%configure --disable-static
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
mkdir -p $RPM_BUILD_ROOT%{_udevrulesdir}
install -p -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_udevrulesdir}

%files
%license COPYING
%doc README
%{_udevrulesdir}/90-mx5000tools.rules
%{_bindir}/mx5000-tool
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so

%changelog
%autochangelog
