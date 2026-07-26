%global source0_hash 2febee044d26770edbc1f8de56d2339a6ed2b69289dcc7ca2b33d21eb3980ef8

Summary:    Script to colorize the compiler output
Name:       colorgcc
Version:    1.4.5
Release:    30%{?dist}
License:    GPL-1.0-or-later
Url:        http://schlueters.de/colorgcc.html
Source0:    https://github.com/colorgcc/colorgcc/archive/%{version}.tar.gz
BuildArch:  noarch
Patch0:     colorgcc-invocation.patch
Patch1:     readme-fedora.patch
BuildRequires:     perl-generators
Requires:   perl-interpreter

%description
Perl script written by Jamie Moyers to colorize the terminal output of C++, CC,
CCACHE, G++, GCC so error messages can be found within longer compiler outputs. 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup
mv ./colorgccrc.txt ./colorgccrc.sample
%patch -P0 -p1
%patch -P1 -p1

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 colorgcc.pl $RPM_BUILD_ROOT/%{_bindir}/color-gcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-g++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-cc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-c++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/color-ccache

ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorgcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorg++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorcc
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorc++
ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT/%{_bindir}/colorccache

install -dm 755 $RPM_BUILD_ROOT%{_libdir}/colorgcc
for n in cc gcc g++ c++ ; do
    ln -s %{_bindir}/color-gcc $RPM_BUILD_ROOT%{_libdir}/colorgcc/$n
done

%files
%{_bindir}/color-gcc
%{_bindir}/color-g++
%{_bindir}/color-cc
%{_bindir}/color-c++
%{_bindir}/color-ccache

%{_bindir}/colorgcc
%{_bindir}/colorg++
%{_bindir}/colorcc
%{_bindir}/colorc++
%{_bindir}/colorccache

%dir %{_libdir}/colorgcc
%{_libdir}/colorgcc/*

%doc README colorgccrc.sample

%changelog
%autochangelog
