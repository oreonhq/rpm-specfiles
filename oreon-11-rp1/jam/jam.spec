%global source0_hash 72ea48500ad3d61877f7212aa3d673eab2db28d77b874c5a0b9f88decf41cb73

# I think it's time we blow this scene
# Get everybody and the stuff together
# Okay, three, two, one, let's jam

Name:		jam
Version:	2.6.1
Release:	4%{?dist}
# https://spdx.org/licenses/Jam.html
License:	Jam
Summary:	Program construction tool, similar to make
URL:		http://public.perforce.com/public/jam/index.html
Source0:	ftp://ftp.perforce.com/jam/%{name}-%{version}.zip
# Submitted upstream by e-mail
Patch0:		jam-2.5-overflow.patch
Patch1:		jam-missing-includes.patch
Patch2:		jam-implicit-int.patch
Patch3:		jam-2.5-argv-fixup.patch
Patch4:		jam-2.6.1-fix-typo.patch
BuildRequires:	gcc
BuildRequires:	byacc
BuildRequires:	make

%description
Jam is a program construction tool, like make. Jam recursively builds target
files from source files, using dependency information and updating actions
expressed in the Jambase file, which is written in jam's own interpreted
language. The default Jambase is compiled into jam and provides a boilerplate
for common use, relying on a user-provide file "Jamfile" to enumerate actual
targets and sources.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .overflows
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1 -b .fixup
%patch -P4 -p1 -b .fix-typo

%build
make CFLAGS="$RPM_OPT_FLAGS" CCFLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m0755 bin.linux*/jam $RPM_BUILD_ROOT/%{_bindir}
install -m0755 bin.linux*/mkjambase $RPM_BUILD_ROOT/%{_bindir}

%files
%doc README RELNOTES *.html
%{_bindir}/jam
%{_bindir}/mkjambase

%changelog
%autochangelog
