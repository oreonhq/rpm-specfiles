%global source0_hash none

Name:           unzoo
Version:        4.4
Release:        38%{?dist}
Summary:        ZOO archive extractor

# Automatically converted from old format: Public Domain - needs further work
License:        LicenseRef-Callaway-Public-Domain
URL:            http://archives.math.utk.edu/software/multi-platform/gap/util/unzoo.c
Source0:        http://archives.math.utk.edu/software/multi-platform/gap/util/unzoo.c

Patch0:         unzoo-convert-strcpy_strcat-to-strncpy_strncat.patch
Patch1:         unzoo-directory-points-backward.patch
Patch2:         unzoo-warning-fixes.patch

BuildRequires:  gcc
%description
'unzoo' is a zoo archive extractor.  A zoo archive is a file that
contains several files, called its members, usually in compressed form
to save space.  'unzoo' can list all or selected members or extract
all or selected members, i.e., uncompress them and write them to
files.  It cannot add new members or delete members.  For this you
need the zoo archiver, called 'zoo', written by Rahul Dhesi.

%prep
%setup -Tc -n %{name}-%{version}
cp -a %{SOURCE0} .
cat %{SOURCE0} | sed -e '/SYNTAX/,/\*\//!d' | cut -c5- > unzoo.txt

%patch -P0 -p1 -b .strncpy
%patch -P1 -p1 -b .revdir
%patch -P2 -p1 -b .warnings

%build
gcc %{optflags} -o unzoo -DSYS_IS_UNIX unzoo.c

%install
rm -rf %{buildroot}

# Install binaries
install -Dpm 755 unzoo %{buildroot}%{_bindir}/unzoo

%files
%{_bindir}/unzoo
%doc unzoo.txt

%changelog
%autochangelog
