%global source0_hash 050062d4f31d307cca52c3f6a7f4b946df8de25fc4bd373e1a5142e41034a7ca
%global gem_name rb-inotify
Name: rubygem-%{gem_name}
Version: 0.10.1
Release:        1%{?dist}
Summary:        A Ruby wrapper for Linux inotify, using FFI
License: MIT
URL: https://github.com/guard/rb-inotify
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildArch: noarch
# oreon:deps
BuildRequires:  /usr/bin/rspec
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(concurrent-ruby)
BuildRequires:  rubygem(ffi)
BuildRequires:  rubygem(rspec-expectations)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
A Ruby wrapper for Linux inotify, using FFI.

%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version}

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
sed -i "/bundler\/setup/ s/^/#/" spec/spec_helper.rb
rspec -rpathname spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rb-inotify-doc -f %{oreon_filedir}/rubygem-rb-inotify-doc.list

%changelog

%autochangelog
