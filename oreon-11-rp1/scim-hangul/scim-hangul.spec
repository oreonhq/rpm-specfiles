%global source0_hash 7f116c87e78da51363fb4968d627364718de6ec02aa6c6119451fdf403e668c0

Name:		scim-hangul
Version:	0.4.0
Release:	12%{?dist}

License:	GPL-3.0-only
URL:		https://github.com/libhangul/scim-hangul
BuildRequires:	make
BuildRequires:	scim-devel >= 1.2.0 libhangul-devel
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
Patch1:     scim-hangul-0.3.2.gcc47.patch
Patch2:     scim-hangul-0.4.0-fixes-gtk2-compile.patch

Summary:	Hangul Input Method Engine for SCIM
Requires:	scim
BuildRequires:  gcc-c++
%ifarch aarch64
BuildRequires:	autoconf
%endif

%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

%build
%ifarch aarch64
autoconf
%endif
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=${RPM_BUILD_ROOT} install

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/hangul*.la

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0/*/IMEngine/hangul.so
%{_libdir}/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%{_datadir}/scim/icons/scim-hangul*.png
%{_datadir}/scim/hangul

%changelog
%autochangelog
