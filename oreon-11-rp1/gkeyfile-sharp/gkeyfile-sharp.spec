%global source0_hash 21a8a7ebfd4cbc2495d2f917426768550fe9dc2dead0e570541dc6a33f181c3d

%define tagname GKEYFILE_SHARP_0_1
%define relvers 0
%define tsuffix g07a401a
%define dsuffix 662c5c1

%global debug_package %{nil}

Name:           gkeyfile-sharp
Version:        0.1
Release:        44%{?dist}
Summary:        C# bindings for glib2's keyfile implementation

# Automatically converted from old format: LGPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2
URL:            http://github.com/mono/%{name}
# Releases are tarballs downloaded from a tag at github.
# They are releases, but the file is generated on the fly.
# The actual URL is: http://github.com/mono/$name/tarball/$tagname
Source0:        mono-%{name}-%{tagname}-%{relvers}-%{tsuffix}.tar.gz
# Upstream patch to fix DllImport name of libglib (BZ 692784)
# https://github.com/mono/gkeyfile-sharp/commit/1a1adb8ec4149b4a0a8e55db0e3baa172cbd2c3f
Patch1:         0001-Change-glib-DllImports-to-libglib-2.0-0.dll.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  glib2-devel
BuildRequires:  gtk-sharp2-devel
BuildRequires:  gtk-sharp2-gapi
BuildRequires:  mono-devel
BuildRequires: make

# Mono only available on these:
ExclusiveArch: %mono_arches

%package devel
Summary:        Development files for gkeyfile-sharp
Requires:       pkgconfig
Requires:       %{name} = %{version}-%{release}

%description
C# bindings for glib2's keyfile implementation

%description devel
Development files for gkeyfile-sharp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mono-%{name}-%{dsuffix}
sed -i "s#gmcs#mcs#g" configure.in
%patch -P1 -p1 -b dllimport-fix

%build
./autogen.sh
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT
chmod 644 `find $RPM_BUILD_ROOT%{_prefix}/lib/mono -name '*.dll.config'`
rm -f $RPM_BUILD_ROOT%{_prefix}/lib/mono/%{name}/%{name}.dll.config

mkdir -p %{buildroot}%{_libdir}/pkgconfig
test "%{_libdir}" = "%{_prefix}/lib" || mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_libdir}/pkgconfig/

%files
%doc AUTHORS ChangeLog LICENSE.LGPL NEWS
%{_prefix}/lib/mono/gac/%{name}
%{_prefix}/lib/mono/%{name}

%files devel
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog
