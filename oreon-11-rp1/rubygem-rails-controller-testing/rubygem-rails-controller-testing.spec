%global source0_hash 741448db59366073e86fc965ba403f881c636b79a2c39a48d0486f2607182e94
%global gem_name rails-controller-testing
Name:           rubygem-%{gem_name}
Version:        1.0.5
Release:        13%{?dist}
Summary:        Extracting `assigns` and `assert_template` from ActionDispatch
License:        MIT
URL:            https://github.com/rails/rails-controller-testing
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         %{name}-rails6.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(railties)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
This gem brings back assigns to your controller tests as well as
assert_template to both controller and integration tests.

%package doc
Summary:        Documentation for %{name}
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
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
sed -i '/^Bundler/ s/^/#/' test/dummy/config/application.rb
ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rails-controller-testing-doc -f %{oreon_filedir}/rubygem-rails-controller-testing-doc.list

%changelog

%autochangelog
