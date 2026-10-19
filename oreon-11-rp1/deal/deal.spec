%global source0_hash af98fc1edba75795ce76c7d2856a0546ca5f26376f36ffa1692af07fd6c62f81
Name: deal
Version: 3.1.12
Release:        1%{?dist}
Summary:        Bridge Hand Generator
URL: https://github.com/gtwilliams/%{name}
Source0:        https://github.com/gtwilliams/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
License: GPL-2.0-or-later AND GPL-1.0-or-later AND BSD-3-Clause-Attribution
Requires: tcl >= 9.0.0
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  perl-podlators
BuildRequires:  tcl-devel
# /oreon:deps
%description
This program generates bridge hands.  It can be told to generate only
hands satisfying conditions like being balanced, having a range of
HCPs, controls, or other user-definable properties.  Hands can be
output in various formats, like pbn for feeding to other bridge
programs, deal itself, or split up into a file per player for
practise.  Extensible via Tcl.

%global build_data %{buildroot}%{_datadir}/%{name}
%global build_docs %{buildroot}%{_docdir}/%{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

touch Make.dep
%set_build_flags
%make_build DATA_DIR=%{_datadir}/%{name}/
%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man6
mkdir -p %{build_data}/ex
mkdir -p %{build_docs}/html
install -p -m 0755 deal     %{buildroot}%{_bindir}
install -p -m 0644 deal.6   %{buildroot}%{_mandir}/man6
install -p -m 0644 deal.tcl %{build_data}
cp -a input     %{build_data}/
cp -a format    %{build_data}/
cp -a lib       %{build_data}/
cp -a ex        %{build_data}/
cp -a docs/html %{build_docs}/
cd %{build_docs}/html/ex ; \
for f in %{build_data}/ex/*.tcl;do \
    if [ -f %{build_docs}/html/ex/$(basename $f .tcl).txt ] && \
       cmp $f %{build_docs}/html/ex/$(basename $f .tcl).txt ; then \
        ln -fs ../../../../%{name}/ex/$(basename $f) $(basename $f .tcl).txt ; \
    fi ; \
done
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
