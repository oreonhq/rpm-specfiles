%global source0_hash 83ced3a3d7f95f67de958d2ce41b1874e83c8d94fe2ddbff50c8b4b82323563a
%global enable_checks 1
%global gem_name deep_merge
Name: rubygem-%{gem_name}
Version: 1.2.2
Release:        11%{?dist}
Summary:        Merge Deeply Nested Hashes
License: MIT
URL: https://github.com/danielsdeleo/deep_merge
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Requires: ruby(rubygems) 
%if 0%{?enable_checks}
%endif
BuildArch: noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Recursively merge hashes. 

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%if 0%{?enable_checks}
ruby -Ilib test/test_deep_merge.rb
%endif
%files -f %{oreon_filedir}/main.list
%files -n rubygem-deep_merge-doc -f %{oreon_filedir}/rubygem-deep_merge-doc.list

%changelog

%autochangelog
