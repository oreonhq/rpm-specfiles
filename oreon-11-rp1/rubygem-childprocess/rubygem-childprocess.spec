%global source0_hash 3616ce99ccb242361ce7f2b19bf9ff3e6bc1d98b927c7edc29af8ca617ba6cd3
%global gem_name childprocess
Name: rubygem-%{gem_name}
Version: 4.1.0
Release:        1%{?dist}
Summary:        A gem for controlling external programs running in the background
License: MIT
URL: http://github.com/enkessler/childprocess
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0: rubygem-childprocess-4.1.0-Make-validates-cleanly-spec-compatible-with-RubyGems-3-5-.patch
BuildArch: noarch
ExclusiveArch: %{ix86} x86_64 noarch
# oreon:deps
BuildRequires:  ruby(release)
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(logger)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem aims at being a simple and reliable solution for controlling external
programs running in the background on any Ruby / OS combination.

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

# ref: https://github.com/enkessler/childprocess/pull/199/
%gemspec_add_dep -g logger

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
sed -i '/[cC]overalls/ s/^/#/' spec/spec_helper.rb
sed -i "/gemspec.validate/ s/^/#/" spec/childprocess_spec.rb
LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec
sed -i '/^\s*it "can write to stdin interactively if duplex = true" do$/ a \
  skip' spec/io_spec.rb
CHILDPROCESS_POSIX_SPAWN=true LC_ALL=C.UTF-8 RUBYOPT=-Ilib rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-childprocess-doc -f %{oreon_filedir}/rubygem-childprocess-doc.list

%changelog

%autochangelog
