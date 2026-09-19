%global source0_hash 0d66c4312147d3e6ed72576715fb883bfa806fbe885d91dcf9f81628d6f0b418

%global pkgname lv2vocoder

Name:		lv2-vocoder-plugins
Version:	1
Release:	36%{?dist}
Summary:	Add a robotic effect to vocals
# Automatically converted from old format: GPLv2 - review is highly recommended.
License:	GPL-2.0-only
URL:		http://download.gna.org/lv2vocoder/
Source0:	http://download.gna.org/lv2vocoder/%{pkgname}-%{version}.tar.bz2

BuildRequires: make
BuildRequires:	gcc-c++
BuildRequires:	lv2-devel
Requires:	lv2

%description
Perhaps you don't know what a vocoder is, but you have heard one before for
sure. Vocoders are often used to add a robotic effect to vocals in music. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{pkgname}-%{version}

# Don't hide anything
sed -i 's|\t@|\t|' GNUmakefile

%build
make %{?_smp_mflags} \
	CFLAGS="-c $RPM_OPT_FLAGS -fPIC -DPIC" \
	LDFLAGS="$RPM_LD_FLAGS"

%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/lv2
make install LV2_INSTALL_PATH="$RPM_BUILD_ROOT%{_libdir}/lv2"

%files
%doc README *.png
%license gpl.txt
%{_libdir}/lv2/*

%changelog
%autochangelog
