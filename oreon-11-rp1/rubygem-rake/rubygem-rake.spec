%global source0_hash 8c9e89d09f66a26a01264e7e3480ec0607f0c497a861ef16063604b1b08eb19c
%global	majorver	13.3.1
%global	rpmminorver	.%(echo %preminorver | sed -e 's|^\\.\\.*||')
%global	fullver	%{majorver}%{?preminorver}
%global	gem_name	rake
%global	baserelease	2
Summary:        Rake is a Make-like program implemented in Ruby
Name:		rubygem-%{gem_name}
Version:	%{majorver}
Release:        1%{?dist}
License:	MIT
URL:		https://github.com/ruby/rake
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1: %{gem_name}-%{version}-tests.txz
BuildArch:	noarch
# oreon:deps
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(minitest)
BuildRequires:  rubygem(test-unit)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
Rake is a Make-like program implemented in Ruby. Tasks and dependencies are
specified in standard Ruby syntax.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch
%description    doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -a 1
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build ./%{gem_name}-%{version}.gemspec
%gem_install
pushd ./%{gem_instdir}
rm -fr \
	Rakefile \
	test/ \
	%{nil}
popd
cp -a \
	Rakefile \
	test/ \
	./%{gem_instdir}
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
        %{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/exe -type f | xargs chmod a+x
pushd %{buildroot}%{gem_instdir}
rm -rf \
	.gitignore .rubocop.yml .travis.yml \
	.github \
	appveyor.yml \
	Gemfile \
	Rakefile \
	rake.gemspec \
	test \
	bin
	%{nil}
popd
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{gem_instdir}/doc/rake.1 %{buildroot}%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

pushd .%{gem_instdir}
sed -i '/bundler/ s/^/#/' Rakefile
export TESTOPTS=--verbose
export VERBOSE=y
export RUBYLIB=$(pwd)/lib
ruby ./exe/rake test
popd
%files -f %{oreon_filedir}/main.list
%files -n rubygem-rake-doc -f %{oreon_filedir}/rubygem-rake-doc.list

%changelog

%autochangelog
