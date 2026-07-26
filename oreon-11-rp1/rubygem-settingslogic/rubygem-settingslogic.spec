%global source0_hash 5925a91d0d48dfb59a6e48ae2bb9c9b801fe6fab25a8e8d302ce8699d92f2ae6

%global gem_name settingslogic

Name:           rubygem-%{gem_name}
Version:        2.0.9
Release:        26%{?dist}
Summary:        Simple settings solution for Ruby

License:        MIT
URL:            https://github.com/binarylogic/settingslogic
Source0:        http://rubygems.org/downloads/%{gem_name}-%{version}.gem
# https://github.com/binarylogic/settingslogic/pull/81
Patch0:         %{name}-rspec3.patch

BuildArch:      noarch
# to avoid jruby
BuildRequires:  ruby
BuildRequires:  rubygems-devel
BuildRequires:  rubygem(rspec)

%description
Settingslogic is a simple configuration and settings solution that uses an ERB
enabled YAML file. Settingslogic works with Rails, Sinatra, or any Ruby
project.

%package doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch

%description doc
Documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gem unpack %{SOURCE0}
%setup -q -D -T -n  %{gem_name}-%{version}
%patch -P0 -p1

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
gem build %{gem_name}.gemspec

%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa ./%{gem_dir}/* %{buildroot}%{gem_dir}/

%check
pushd .%{gem_instdir}
rspec -Ilib spec
popd

%files
%doc %{gem_instdir}/LICENSE
%dir %{gem_instdir}
%{gem_libdir}
%exclude %{gem_cache}
%exclude %{gem_instdir}/spec
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/%{gem_name}.gemspec
%exclude %{gem_instdir}/Gemfile
%exclude %{gem_instdir}/Gemfile.lock
%exclude %{gem_instdir}/Rakefile
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/README.rdoc

%changelog
%autochangelog
