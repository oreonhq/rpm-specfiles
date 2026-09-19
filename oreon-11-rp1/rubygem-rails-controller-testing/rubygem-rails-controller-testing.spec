%global source0_hash 741448db59366073e86fc965ba403f881c636b79a2c39a48d0486f2607182e94

%global gem_name rails-controller-testing

Name:           rubygem-%{gem_name}
Version:        1.0.5
Release:        13%{?dist}
Summary:        Extracting `assigns` and `assert_template` from ActionDispatch

License:        MIT
URL:            https://github.com/rails/rails-controller-testing
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
# https://github.com/rails/rails-controller-testing/pull/65
Patch0:         %{name}-rails6.patch

BuildRequires:  ruby(release)
BuildRequires:  rubygems-devel
BuildRequires:  ruby >= 2.2.2
BuildRequires:  rubygem(railties) >= 5.0.1
#BuildRequires:  rubygem(sqlite3)
BuildArch:      noarch

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
# Create the gem as gem install only works on a gem file
gem build ../%{gem_name}-%{version}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
# kill the bundler
sed -i '/^Bundler/ s/^/#/' test/dummy/config/application.rb

ruby -Itest -e 'Dir.glob "./test/**/*_test.rb", &method(:require)'
popd

%files
%license %{gem_instdir}/LICENSE
%dir %{gem_instdir}/
%{gem_libdir}/
%{gem_spec}
%exclude %{gem_cache}

%files doc
%doc %{gem_docdir}/
%doc %{gem_instdir}/README.md
%{gem_instdir}/test/
%{gem_instdir}/Rakefile

%changelog
%autochangelog
