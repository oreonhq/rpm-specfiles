%global source0_hash 390a5102440b2c127b501754eb76fd93d08851e8c84f680d3cc378da9fadf1c7

# FIXME: Patch to fix for increased safety
%global build_type_safety_c 0

%global commit 49457116bb0796636fd1bc84f39006fb102bfafc
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global commitdate 20161025

Name:           glimpse
Version:        4.12.6^git%{commitdate}.%{shortcommit}
Release:        4%{?dist}
Summary:        Powerful file indexing and query system

License:        ISC
URL:            https://github.com/gvelez17/glimpse
Source0:        %{url}/archive/%{commit}/%{name}-%{commit}.tar.gz

# From Debian
Patch0:         fix-makefile.patch
Patch1:         fix-makefile-cc-var.patch
Patch2:         agrep-fix-double-free.patch

BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  flex
BuildRequires:  gcc
%if 0%{?rhel} && 0%{?rhel} < 9
BuildRequires:  flex-devel
%else
BuildRequires:  libfl-static
%endif
BuildRequires:  make
Requires:       agrep

%description
Glimpse is a very powerful indexing and query system that allows you to
search through all your files very quickly.  It can be used by
individuals for their personal file systems as well as by organizations
for large data collections.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{commit} -p1

%build
autoconf
%configure
# Parallel make breaks it
make DEBUGFLAGS="%{build_cflags}" OTHERLIBS="%{build_ldflags}"

%install
make install prefix="%{buildroot}%{_prefix}" exec_prefix="%{buildroot}%{_prefix}" manprefix="%{buildroot}%{_mandir}"

# Move undocumented commands to libexec
mkdir -p %{buildroot}%{_libexecdir}/%{name}
mv %{buildroot}%{_bindir}/*cast %{buildroot}%{_bindir}/tbuild %{buildroot}%{_bindir}/wgconvert %{buildroot}%{_libexecdir}/%{name}

# Drop agrep, as we have another provider for it
rm -v %{buildroot}%{_bindir}/agrep %{buildroot}%{_mandir}/man1/agrep.1*

%files
%license LICENSE
%doc README KNOWN_BUGS ChangeLog CHANGES
%{_bindir}/glimpse*
%{_mandir}/man1/glimpse*
%{_libexecdir}/glimpse/

%changelog
%autochangelog
