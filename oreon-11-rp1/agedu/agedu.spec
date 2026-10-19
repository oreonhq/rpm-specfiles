%global source0_hash 432dd9602df326088956b3e4f5efe656ad09777873d38695e0d68810899941c2
%global rel 20200705.2a7d4a2
Name:           agedu
Version:        20260410.3622eda
Release:        1%{?dist}
Summary:        An utility for tracking down wasted disk space
License:        MIT
URL:            http://www.chiark.greenend.org.uk/~sgtatham/agedu/
Source0:        http://www.chiark.greenend.org.uk/~sgtatham/%{name}/%{name}-%{rel}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
Agedu is a program that helps you to track down wasted disk space by creating
a graphical representation of last access times and occupied disk space of
files and directories.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{rel}

%build

%configure
make %{?_smp_mflags}
%install
%make_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
