%global source0_hash c322df90b74e3b0525c4e09c7d1aa0781a3a5229f34ad78eaccfe1948361bb92

Name:           scim-thai
Version:        0.1.3
Release:        24%{?dist}
Summary:        Thai Input Method Engine for SCIM

License:        GPL-2.0-or-later
URL:            http://linux.thai.net/projects/scim-thai
Source0:        ftp://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.gz
Patch0:         scim-thai-fixes-setup-dialog.patch

BuildRequires:  make
BuildRequires:  gcc-c++
BuildRequires:  scim-devel, libthai-devel
%ifarch aarch64
BuildRequires:	autoconf
%endif
Requires:       scim

%description
SCIM-Thai is a SCIM IMEngine module for Thai, based on the libthai library.

Currently, it supports Ketmanee, TIS-820.2538, and Pattachote keybaord layouts
and can validate input sequences at 3 levels of strictness.

For applications that support surrounding text retrieval/deleting,
it also corrects invalid input sequences.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%ifarch aarch64
autoconf
%endif
%configure --disable-static
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/{IMEngine,SetupUI}/thai*.la
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING README ChangeLog
%{_libdir}/scim-1.0/*/IMEngine/thai.so
%{_libdir}/scim-1.0/*/SetupUI/thai-imengine-setup.so
%{_datadir}/scim/icons/scim-thai.png

%changelog
%autochangelog
