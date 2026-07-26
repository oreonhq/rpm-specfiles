%global source0_hash 7e5f02f7761299dfbc9409565a915b6241baa05f8452cb0ca9bb3d2446c8d60f

Name:		python-utmp
Version:	0.8.2
Release:	33%{?dist}
Summary:	Python modules for umtp records

License:	LicenseRef-Fedora-UltraPermissive
URL:		http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/
Source0:	http://kassiopeia.juls.savba.sk/~garabik/software/python-utmp/%{name}_%{version}.tar.gz

# Need to change the name of the shared library we create, so it is the same as the name
# of the module we import, or else Python will not be able to import it.
# And use the correct include paths.
Patch0:         patch-make.diff

BuildRequires: make
BuildRequires:  gcc
BuildRequires:  pkgconf

%global _description %{expand:
python-utmp consists of three modules, providing access to utmp records.
It is quite difficult to access utmp record portably, because every UNIX
has different structure of utmp files. Currently, python-utmp works on
platforms which provide getutent, getutid, getutline, pututline,
setutent, endutent and utmpname functions (such as GNU systems
(Linux and hurd) and System V unices) and on BSD systems using
simple utmp structure.}

%description %_description

%package -n python3-utmp
Summary:        Python modules for umtp records
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-utmp}

%description -n python3-utmp %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name} -p1

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

%files -n python3-utmp
%license COPYING
%doc README TODO
%{python3_sitearch}/*

%changelog
%autochangelog
