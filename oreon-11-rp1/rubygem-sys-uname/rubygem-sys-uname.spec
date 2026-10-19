%global source0_hash 4c26d36b66746872a14b050015f4c22ce43f493a205ab1eeb50054976711663e
%global gem_name sys-uname
Name: rubygem-%{gem_name}
Version: 1.2.2
Release:        1%{?dist}
Summary:        An interface for returning uname (platform) information
License: Apache-2.0
URL: http://github.com/djberg96/sys-uname
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:  sys-uname-pr23-remove-ostruct-dep.patch
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
The sys-uname library provides an interface for gathering information
about your current platform. The library is named after the Unix 'uname'
command but also works on MS Windows. Available information includes
OS name, OS version, system name and so on. Additional information is
available for certain platforms.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}
%patch -P0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-sys-uname-doc -f %{oreon_filedir}/rubygem-sys-uname-doc.list

%changelog

%autochangelog
