%global source0_hash 37f41e617274a0ab714fb85b57da24ce0c29e24fcf373fec80eb99b6464ca2fb

%define tagname GUDEV_SHARP_0_1
%define relvers 0
%define tsuffix g2c53e2f
%define dsuffix cd3e7df

%global debug_package %{nil}

Name:           gudev-sharp
Version:        0.1
Release:        42%{?dist}
# This is necessary because we went to 3.0 too soon.
Epoch:          1
Summary:        C# bindings for gudev

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://github.com/mono/%{name}
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname
Source0:        mono-%{name}-%{tagname}-%{relvers}-%{tsuffix}.tar.gz

BuildRequires:  mono-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libgudev1-devel
BuildRequires:  gtk2-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires: make

# Mono only available on these:
ExclusiveArch: %mono_arches

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

%files
%doc AUTHORS ChangeLog LICENSE.LGPL NEWS
%{_prefix}/lib/mono/gac/%{name}
%{_prefix}/lib/mono/%{name}-1.0

%files devel
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
%autochangelog
