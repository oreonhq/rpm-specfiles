%global source0_hash 80fc9c47a9b640d6834e0dc7b3c94c9df37f08cb072b7761e4a71e22cff29b33
%global gem_name ruby-progressbar
Name:           rubygem-%{gem_name}
Version:        1.13.0
Release:        1%{?dist}
Summary:        Ruby/ProgressBar is a flexible text progress bar library
License:        MIT
URL:            https://github.com/jfelchner/ruby-progressbar
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:        %{name}-%{version}-testsuite.tar.gz
Source2:        ruby-progressbar-create-test-suite-tarball.sh
BuildArch:      noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(timecop)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Ruby/ProgressBar is an extremely flexible text progress bar library for Ruby.
The output can be customized with a flexible formatting system including:
percentage, bars of various formats, elapsed time and estimated time
remaining.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}
BuildArch:      noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1

pushd %{gem_name}-%{version}/
# rspectacular does nothing significant, removing
sed -i spec/spec_helper.rb -e '\@rspectacular@d'
popd
cp -a %{gem_name}-%{version}/spec .

%build

gem build ../%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* %{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -f \
	Rakefile \
	%{nil}
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

rm -rf .%{gem_instdir}/spec
cp -a spec .%{gem_instdir}
pushd .%{gem_instdir}
export RUBYLIB=$(pwd)/lib
sed -i spec/lib/ruby-progressbar/base_spec.rb \
	-e '\@can be converted into a hash@s|it|xit|'
sed -i spec/lib/ruby-progressbar/projector/smoothed_average_spec.rb \
	-e 's|\.to be \([0-9][0-9]*\.[0-9][0-9]*\)|.to eq(\1)|'
ruby -rruby-progressbar -rtimecop -S rspec spec
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-ruby-progressbar-doc -f %{oreon_filedir}/rubygem-ruby-progressbar-doc.list

%changelog

%autochangelog
