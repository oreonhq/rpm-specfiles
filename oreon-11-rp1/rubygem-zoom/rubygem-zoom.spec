%global source0_hash f6a6479e691d2373a0db5c18be333a32396220816ec52e1116e6bcda390361cb

%define		gem_name		zoom

Name:		rubygem-%{gem_name}
Version:	0.5.0
Release:	38%{?dist}
Summary:	Ruby binding to ZOOM

# README.md
# SPDX confirmed
License:	LGPL-2.1-only
URL:		https://github.com/bricestacey/ruby-zoom
Source0:	https://rubygems.org/gems/%{gem_name}-%{version}.gem

BuildRequires:	ruby(release)
BuildRequires:	rubygem(rake)
BuildRequires:	ruby-devel
BuildRequires:	rubygems-devel

BuildRequires:	gcc
BuildRequires:	libgcrypt-devel
BuildRequires:	libgpg-error-devel
BuildRequires:	libxslt-devel
BuildRequires:	libyaz-devel

BuildRequires:	rubygem(test-unit)

Requires:	ruby(rubygems)

Provides:	rubygem(%{gem_name}) = %{version}-%{release}
# Obsolete but not provide
# Obsoletes: ruby(zoom) < 0.3.0 does not obsolete ruby-zoom
Obsoletes:	ruby-zoom < 0.3.0

%description
Ruby/ZOOM provides a Ruby binding to the Z39.50 Object-Orientation 
Model (ZOOM), an abstract object-oriented programming interface 
to a subset of the services specified by the Z39.50 standard, 
also known as the international standard ISO 23950.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}

%description	doc
This package contains documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
mv ../%{gem_name}-%{version}.gemspec .

%{_fixperms} .

%build
gem build %{gem_name}-%{version}.gemspec
%gem_install

find . -type f -print0 | xargs --null chmod ugo+r

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a ./%{gem_dir}/* %{buildroot}%{gem_dir}/

mkdir -p %{buildroot}%{gem_extdir_mri}
cp -a ./%{gem_extdir_mri}/* %{buildroot}%{gem_extdir_mri}/

rm -f %{buildroot}%{gem_cache}
pushd %{buildroot}%{gem_extdir_mri}
rm -f \
	gem_make.out \
	mkmf.log \
	%{nil}
popd

# clean the built bits out
pushd %{buildroot}%{gem_instdir}
rm -rf  \
	Rakefile \
	%{gem_name}.gemspec \
	ext/ \
	test/ \
	%{nil}
popd

%check
# Net connection needed, disabling now.
#ping -c 3 fedoraproject.org || exit 0
pushd .%{gem_instdir}

ruby \
	-Ilib:.:%{buildroot}%{gem_extdir_mri} -rzoom -rtest/unit \
	test/*_test.rb

popd

%files
%dir	%{gem_instdir}/
%doc	%{gem_instdir}/ChangeLog
%license	%{gem_instdir}/README.md

%dir	%{gem_extdir_mri}
%{gem_extdir_mri}/*

%{gem_spec}

%files doc
%{gem_docdir}/
%{gem_instdir}/sample/

%changelog
%autochangelog
