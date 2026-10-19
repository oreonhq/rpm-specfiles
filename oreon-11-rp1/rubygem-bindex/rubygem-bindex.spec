%global source0_hash 7b1ecc9dc539ed8bccfc8cb4d2732046227b09d6f37582ff12e50a5047ceb17e
%global gem_name bindex
Name: rubygem-%{gem_name}
Version: 0.8.1
Release:        1%{?dist}
Summary:        Bindings for your Ruby exceptions
License: MIT
URL: https://github.com/gsamokovarov/bindex
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-bindex-0.8.1-Fix-compatibility-with-Minitest-5.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  ruby(release)
BuildRequires:  ruby-devel
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Bindings for your Ruby exceptions.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

%patch 0 -p1

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{gem_extdir_mri}/skiptrace/internal/
cp -a .%{gem_extdir_mri}/gem.build_complete %{buildroot}%{gem_extdir_mri}/
cp -a .%{gem_extdir_mri}/skiptrace/internal/*.so %{buildroot}%{gem_extdir_mri}/skiptrace/internal/
rm -rf %{buildroot}%{gem_instdir}/ext/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
ruby -I$(dirs +1)%{gem_extdir_mri}:lib:test -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-bindex-doc -f %{oreon_filedir}/rubygem-bindex-doc.list

%changelog

%autochangelog
