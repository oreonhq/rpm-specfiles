%global source0_hash 9e8be7aca97ef31ecc7af845954caddf52f9dad4d28ee1392dca829b75e64085
%global _R_libdir_check %{nil}
Name:           R-littler
Version:        %R_rpm_version 0.3.21
Release:        1%{?dist}
Summary:        littler: R at the Command-Line via 'r'
License:        GPL-2.0-or-later
URL:            %{cran_url}
Source0:        https://cran.r-project.org/package=littler&version=%{version}#/littler_%{version}.tar.gz
# oreon:deps
BuildRequires:  R-devel
# /oreon:deps
%description
A scripting and command-line front-end is provided by 'r' (aka 'littler')
as a lightweight binary wrapper around the GNU R language and environment
for statistical computing and graphics. While R can be used in batch
mode, the r binary adds full support for both 'shebang'-style scripting
(i.e. using a hash-mark-exclamation-path expression as the first line in
scripts) as well as command-line use in standard Unix pipelines. In other
words, r provides the R language without the environment.

%package examples
Summary:        R-littler Examples
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description examples
Examples for using R-littler.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c
chmod +x littler/inst/examples/installDeps2.r

%build

%install
%R_install
rm -rf %{buildroot}%{_R_libdir}/littler/script-tests
mkdir -p %{buildroot}%{_bindir}
ln -rs %{buildroot}%{_R_libdir}/littler/bin/r %{buildroot}%{_bindir}/r
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_R_libdir}/littler/man-page/r.1 %{buildroot}%{_mandir}/man1
rmdir %{buildroot}%{_R_libdir}/littler/man-page
for f in %{buildroot}%{_R_libdir}/littler/examples/* ; do
    grep -q '/usr/bin/env r' $f && sed 's!/usr/bin/env r!/usr/bin/r!' -i $f
done
%R_save_files
grep -v examples %{R_files} > %{R_files}.main
grep examples %{R_files} > %{R_files}.examples
%oreon_autofiles R-littler-examples usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%R_check
%files -f %{oreon_filedir}/main.list
%files -n R-littler-examples -f %{oreon_filedir}/R-littler-examples.list

%changelog

%autochangelog
