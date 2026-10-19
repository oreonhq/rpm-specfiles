%global source0_hash 7a77b97a92c787e2aa3fbc4a1239afc3342c781151dc98cfb81461b3b7cad10f
%global gem_name json_spec
Name:           rubygem-%{gem_name}
Version:        1.1.5
Release:        1%{?dist}
Summary:        Easily handle JSON in RSpec and Cucumber
License:        MIT
URL:            https://github.com/collectiveidea/json_spec
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Patch0:         %{name}-ruby24.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(multi_json)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
RSpec matchers and Cucumber steps for testing JSON content.

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

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

# remove developer-only files
for f in .gitignore .travis.yml Gemfile Rakefile gemfiles/*; do
  rm $f
  sed -i "s|\"$f\"\(.freeze\)\?,\?||g" %{gem_name}.gemspec
done

%build

gem build %{gem_name}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
rspec -Ilib spec
cucumber --tags "not @fail"
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-json_spec-doc -f %{oreon_filedir}/rubygem-json_spec-doc.list

%changelog

%autochangelog
