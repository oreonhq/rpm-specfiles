%global source0_hash 8332234eab873a6554f1eaa2174a511958d290c8f0944592c6da090cbd221ace
%global gitrev bb0ae
%global posttag git%{gitrev}
%global snapshot %{version}-%{posttag}
Name:       pybugz
Summary:        Command line interface for Bugzilla written in Python
Version:    0.14
Release:        1%{?dist}
License:    GPL-2.0-only
URL:        https://github.com/williamh/pybugz
BuildArch:  noarch
Requires:       python3
Patch0: pybugz-0.13-gitbb0ae-rh-default.patch
Patch1: pybugz-0.13-gitbb0ae-limit-configurable.patch
%if 0%{?bash_completion}
%endif
Source0:        %{name}-%{snapshot}.tar.gz
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
Pybugz was conceived as a tool to speed up the work-flow for Gentoo Linux
contributors when dealing with bugs using Bugzilla.  By avoiding the clunky web
interface, the user can search, isolate and contribute to the project very
quickly.  Developers alike can easily extract attachments and close bugs
comfortably from the command line.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{snapshot}

%build

%{__python3} setup.py build
%install
%{__python3} setup.py install --root=%{buildroot}
%global bash_cmpl_dir %(pkg-config --variable=completionsdir bash-completion)
%if 0%{?bash_completion}
  mkdir -p %{buildroot}%{bash_cmpl_dir}
  cp %{_builddir}/%{name}-%{snapshot}/contrib/bash-completion \
     %{buildroot}%{bash_cmpl_dir}/bugz
%endif
mkdir -p %{buildroot}%{_mandir}/man1
cp man/bugz.1 %{buildroot}%{_mandir}/man1/bugz.1
mkdir -p %{buildroot}%{_docdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
