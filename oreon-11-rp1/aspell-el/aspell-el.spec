%global source0_hash 3f6508937dcaa64a6c70ee5f722f088b46b202a6409961b93b705d4ec4f56380
%define lang el
%define langrelease 3
Summary:        Greek dictionaries for Aspell
Name: aspell-%{lang}
Epoch: 50
Version: 0.50
Release:        1%{?dist}
License: GPL-2.0-only
URL: http://aspell.net/
Source0:        https://ftp.gnu.org/gnu/asp%{lang}l/dict/%{lang}/%{name}-%{version}-%{langrelease}.tar.bz2
Provides:  deprecated()
Requires: aspell >= 12:0.60
%define debug_package %{nil}
# oreon:deps
BuildRequires:  aspell
BuildRequires:  make
# /oreon:deps
%description
Provides the word list/dictionaries for the following: Greek

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n aspell-%{lang}-%{version}-%{langrelease}

%build

./configure
make
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
