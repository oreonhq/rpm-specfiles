%global source0_hash 230c84d7792ed38003481eacb995845f205bc591a69883eae4acd028679e50f3
Name: cfdg
Version:  3.4.3
Release:        1%{?dist}
Summary:        Context Free Design Grammar
License: GPL-2.0-or-later
URL: http://www.contextfreeart.org/
Source0:        http://www.contextfreeart.org/download/ContextFreeSource%{version}.tgz
Patch0:  cfdg-nostrip.patch
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libatomic
BuildRequires:  libicu-devel
BuildRequires:  libpng-devel
BuildRequires:  make
BuildRequires:  sed
# /oreon:deps
%description
Context Free is a program that generates images from written instructions 
called a grammar. The program follows the instructions in a few seconds to 
create images that can contain millions of shapes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qcn ContextFreeSource%{version}

%patch -P0 -p1

# Remove -march=native everywhere.
find -type f -print0 | xargs -0 sed -i 's/-march=native//g'

%build

OPTFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}
%install
install -D -m 755 cfdg %{buildroot}%{_bindir}/cfdg
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
