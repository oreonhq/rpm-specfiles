%global source0_hash 37f41e617274a0ab714fb85b57da24ce0c29e24fcf373fec80eb99b6464ca2fb
%define tagname GUDEV_SHARP_0_1
%define relvers 0
%define tsuffix g2c53e2f
%define dsuffix cd3e7df
%global debug_package %{nil}
Name:           gudev-sharp
Version:        0.1
Release:        1%{?dist}
Epoch:          1
Summary:        C# bindings for gudev
License:        LicenseRef-Callaway-LGPLv2
URL:            http://github.com/mono/%{name}
Source0:        mono-%{name}-%{tagname}-%{relvers}-%{tsuffix}.tar.gz
ExclusiveArch: %mono_arches
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  gtk2-devel
BuildRequires:  libgudev1-devel
BuildRequires:  make
BuildRequires:  mono-devel
# /oreon:deps
%package devel
Summary:        Development files for gudev-sharp
Requires:	pkgconfig
Requires:       %{name} = %{epoch}:%{version}-%{release}
%description
C# bindings for gudev

%description devel
Development files for gudev-sharp

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mono-%{name}-%{dsuffix}

sed -i "s#gmcs#mcs#g" configure.in

%build

sed -i 's|^\./configure.*||' autogen.sh # Remove the configure step, we'll do it manually
./autogen.sh
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 `find $RPM_BUILD_ROOT%{_prefix}/lib/mono -name '*.dll.config'`
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mono/%{name}-1.0/%{name}.dll.config
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv $RPM_BUILD_ROOT/%{_prefix}/lib/pkgconfig/* $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gudev-sharp-devel -f %{oreon_filedir}/gudev-sharp-devel.list

%changelog

%autochangelog
