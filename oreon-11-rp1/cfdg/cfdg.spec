%global source0_hash b357cfa9f4f1ee47fd3d7397c855fd9431e67a08c4901f242f205e1010e36e16

Name: cfdg
Version:  3.4.2
Release:  5%{?dist}
Summary: Context Free Design Grammar

License: GPL-2.0-or-later
URL: http://www.contextfreeart.org/

Source0: http://www.contextfreeart.org/download/ContextFreeSource%{version}.tgz
Patch0:  cfdg-nostrip.patch
BuildRequires: gcc-c++ libatomic libicu-devel
BuildRequires: libpng-devel bison flex
BuildRequires: make
BuildRequires: sed

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
#pushd ContextFreeSource%{version}
OPTFLAGS=$RPM_OPT_FLAGS make %{?_smp_mflags}
#popd

%install
#pushd ContextFreeSource%{version}
install -D -m 755 cfdg %{buildroot}%{_bindir}/cfdg
#popd

%files
%{_bindir}/cfdg
%license LICENSE.txt
%doc input/* README* ChangeLog

%changelog
%autochangelog
