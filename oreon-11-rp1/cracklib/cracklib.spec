%global source0_hash 877b823198eb29aa1778b16a70cad05f7b54b164b3bf7ab656fc326c393f4c85
%global source1_hash 1d9dd4d8eed30520d83c0f331ac8ddad5b0c78b9fe8a4f456edbba7b6f871250

Name: cracklib
Version: 2.10.3
Release: 1%{?dist}
Summary: Password strength checking library
License: LGPL-2.1-or-later
URL: https://github.com/cracklib/cracklib
Source0: https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-%{version}.tar.gz
Source1: https://github.com/cracklib/cracklib/releases/download/v%{version}/cracklib-words-%{version}.gz

BuildRequires: gcc
BuildRequires: make
BuildRequires: zlib-devel
BuildRequires: oreon-rpm-macros

%description
A library that checks whether a password is based on a dictionary word. OpenLDAP uses it.

%package devel
Summary: Development files for cracklib
Requires: cracklib%{?_isa} = %{version}-%{release}

%description devel
Headers and the pkgconfig file for cracklib.

%package dicts
Summary: Default cracklib wordlist
Requires: cracklib%{?_isa} = %{version}-%{release}

%description dicts
The packed default wordlist cracklib searches.

%prep
%autosetup -n cracklib-%{version} -p1
%oreon_sha256
echo '%{source1_hash}  %{SOURCE1}' | sha256sum -c -

%build
%oreon_configure --disable-static --with-pic
%oreon_make

%install
%oreon_make_install
find %{buildroot} -name '*.la' -delete
mkdir -p %{buildroot}%{_datadir}/cracklib
gzip -cd %{SOURCE1} | ./util/cracklib-format | ./util/cracklib-packer %{buildroot}%{_datadir}/cracklib/pw_dict
%oreon_filelist_devel
grep -v '/share/cracklib/' %{_builddir}/%{name}.files > %{_builddir}/%{name}.files.tmp
mv %{_builddir}/%{name}.files.tmp %{_builddir}/%{name}.files

%files -f %{_builddir}/%{name}.files
%license COPYING.LIB

%files devel -f %{_builddir}/%{name}-devel.files

%files dicts
%{_datadir}/cracklib
