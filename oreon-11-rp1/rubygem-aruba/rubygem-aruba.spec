%global source0_hash 837a2f023368a75a38ad9be227e9738ab9af7df3b3f35afd8fb5fc5f7a93f1d4
%global     gem_name    aruba
Summary:        CLI Steps for Cucumber, hand-crafted for you in Aruba
Name:       rubygem-%{gem_name}
Version:    2.3.3
Release:        1%{?dist}
License:        MIT
URL:            https://github.com/cucumber/aruba
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-testsuite.tar.gz
Source2:        %{gem_name}-create-test-suite-tarball.sh
Patch1:         rubygem-aruba-2.0.0-make-bundler-optional.patch
Patch2:         rubygem-aruba-2.3.1-diff-lcs-1_6-change.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  less
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(childprocess)
BuildRequires:  rubygem(contracts)
BuildRequires:  rubygem(cucumber)
BuildRequires:  rubygem(irb)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(thor)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Aruba is Cucumber extension for Command line applications written
in any programming language.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description doc
Documentation for %{name}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
pushd %{gem_name}-%{version}
for f in *
do
    basef=$(basename $f)
    target=../${basef}
    ln -sf $(pwd)/$f $target
done
# For tests
ln -sf ../lib
popd
%patch -P1 -p1
%patch -P2 -p1 -R

mv ../%{gem_name}-%{version}.gemspec .

# Relax cucumber dependency
# Partially revert https://github.com/cucumber/aruba/pull/906
sed -i '\@cucumber@s|>= 8.0|>= 7.0|' %{gem_name}-%{version}.gemspec
# Remove bundler dependency harder
sed -i '\@dependency.*bundler@d' %{gem_name}-%{version}.gemspec

%build

gem build %{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
    %{buildroot}%{gem_dir}/
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd %{gem_name}-%{version}
for f in *
do
    basef=$(basename $f)
    target=../%{gem_instdir}/${basef}
    unlink $target || true
    ln -sf $(pwd)/$f $target
done
popd
pushd .%{gem_instdir}
sed -i spec/spec_helper.rb \
    -e '\@[sS]imple[Cc]ov@d' \
    %{nil}
env RUBYOPT=-rtime \
    rspec spec
sed -i features/support/env.rb \
    -e '\@require.*simplecov@d'
> features/support/simplecov_setup.rb
sed -i fixtures/cli-app/spec/spec_helper.rb \
    -e "\@\$LOAD_PATH@s|\.\./\.\./lib|$(pwd)/lib|"
sed -i features/step_definitions/hooks.rb \
	-e '\@platform.which@s|"python"|"no-python"|'
PPC64_ENV_P=$(uname -m | grep -q ppc64 && echo 0 || echo 1)
if test x"${PPC64_ENV_P}" == x0
then
    mv features/04_aruba_api/filesystem/report_disk_usage.feature{,.skip}
fi
mv features/03_testing_frameworks/cucumber/disable_bundler.feature{,.skip}
sed -i features/04_aruba_api/core/expand_path.feature -e "s|/home/\[\^/\]+|$(echo $HOME)|" 
sed -i features/02_configure_aruba/home_directory.feature \
    -e "\@Scenario: Default value@,\@Scenario@s|/home/|$(echo $HOME)|"
sed -i features/02_configure_aruba/home_directory.feature \
    -e "\@Set to aruba's working directory@,\@Scenario@s|/home/|$(echo $HOME)/|"
export CUCUMBER_PUBLISH_QUIET=true
env RUBYOPT=-I$(pwd)/lib cucumber -f progress
if test x"${PPC64_ENV_P}" == x0
then
    mv features/04_aruba_api/filesystem/report_disk_usage.feature{.skip,}
fi
mv features/03_testing_frameworks/cucumber/disable_bundler.feature{.skip,}
popd # from .%%{gem_instdir}
%files -f %{oreon_filedir}/main.list
%files -n rubygem-aruba-doc -f %{oreon_filedir}/rubygem-aruba-doc.list

%changelog

%autochangelog
