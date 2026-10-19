%global source0_hash 4b44a933a776500937887134cf89b94a89199304c416ad05b2ac365cce1076d8
Name:           pkgdiff
Version:        1.8
Release:        1%{?dist}
Summary:        A tool for analyzing changes in Linux software packages
License:        GPL-2.0-or-later
URL:            http://lvc.github.io/pkgdiff/
Source0:        https://github.com/lvc/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl-interpreter >= 5.8
Requires:       diffutils
Requires:       wdiff
Requires:       binutils
Requires:       gawk
Requires:       rpm
Requires:       abi-compliance-checker >= 1.99.1
Requires:       abi-dumper >= 0.97
# oreon:deps
BuildRequires:  help2man
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Copy)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Package Changes Analyzer (pkgdiff) is a tool for analyzing changes
in Linux software packages (RPM, DEB, TAR.GZ, etc). The tool is
intended for Linux maintainers who are interested in ensuring
compatibility of old and new versions of packages.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod 0644 LICENSE README.md
chmod 0755 %{name}.pl

%build

%install
mkdir -p %{buildroot}%{_prefix}
mkdir -p %{buildroot}%{_mandir}/man1
perl Makefile.pl -install --prefix=%{_prefix} --destdir=%{buildroot}
cp %{name}.pl %{name}
help2man -N --no-discard-stderr -o %{name}.1 ./%{name}
sed -i 's/\(.\)/\n\1/' %{name}.1
sed -i 's/PACKAGE/PKGDIFF/g' %{name}.1
install -m 0644 %{name}.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
