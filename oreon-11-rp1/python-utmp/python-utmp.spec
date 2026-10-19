%global source0_hash 48895709fc345fea10aa2236501f6c6a07d8acaf92191dc23a4781cde8098082
Name:		python-utmp
Version:	0.9.orig
Release:        1%{?dist}
Summary:        Python modules for umtp records
License:	LicenseRef-Fedora-UltraPermissive
URL:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:        http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/%{name}_%{version}.tar.gz
Patch0:         patch-make.diff
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconf
BuildRequires:  python3-devel
# /oreon:deps
%description

%package -n python3-utmp
Summary:        Python modules for umtp records
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-utmp}
%description -n python3-utmp

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%set_build_flags
make -f Makefile.glibc \
	DEFINES=" \
		-D_HAVE_UT_SESSION -D_HAVE_UT_ADDR_V6 -D_HAVE_UT_EXIT \
		-D_HAVE_UT_HOST -D_HAVE_UT_ID -D_HAVE_UT_TV -D_HAVE_UT_USER \
		-D_HAVE_UTMPNAME -D_HAVE_SETUTENT -D_HAVE_GETUTENT -D_HAVE_ENDUTENT \
		-D_HAVE_GETUTID -D_HAVE_GETUTLINE -D_HAVE_PUTUTLINE \
		%{optflags}" \
	PYTHONPKGVER=3 \
	PYTHONVER=%{python3_version} \
	PYTHONINCLUDE=/usr/include/python%{python3_version}/
%install
make \
	PYTHONDIR=%{buildroot}/%{python3_sitearch}/ \
	PYTHONVER=%{python3_version} \
	install
rm -f COPYING
install -D -p -m644 debian/copyright COPYING
%oreon_autofiles python3-utmp usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-utmp -f %{oreon_filedir}/python3-utmp.list

%changelog

%autochangelog
