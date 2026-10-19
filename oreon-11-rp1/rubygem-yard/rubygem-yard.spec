%global source0_hash 721fb82afb10532aa49860655f6cc2eaa7130889df291b052e1e6b268283010f
%global	gem_name	yard
Name:		rubygem-%{gem_name}
Version:	0.9.38
Release:        3%{?dist}
Summary:        Documentation tool for consistent and usable documentation in Ruby
License:	MIT AND (MIT OR Ruby) AND BSD-2-Clause AND (GPL-2.0-only OR Ruby)
URL:		http://yardoc.org
Source0:        https://rubygems.org/gems/%{gem_name}-%{version}.gem
Source1:	%{gem_name}-%{version}-test-missing-files.tar.gz
Source2:	yard-create-missing-test-files.sh
Patch0:	yard-0.9.38-issue1637-spec-namespace-collision.patch
Recommends:	rubygem(irb)
BuildArch:		noarch
# oreon:deps
BuildRequires:  /usr/bin/rackup
BuildRequires:  ruby
BuildRequires:  ruby(release)
BuildRequires:  rubygem(RedCloth)
BuildRequires:  rubygem(asciidoctor)
BuildRequires:  rubygem(bundler)
BuildRequires:  rubygem(irb)
BuildRequires:  rubygem(rack)
BuildRequires:  rubygem(rake)
BuildRequires:  rubygem(redcarpet)
BuildRequires:  rubygem(rspec)
BuildRequires:  rubygem(webrick)
BuildRequires:  rubygems-devel
# /oreon:deps
%description
YARD is a documentation generation tool for the Ruby programming language.
It enables the user to generate consistent, usable documentation that can be
exported to a number of formats very easily, and also supports extending for
custom Ruby constructs such as custom class level definitions.

%package	doc
Summary:	Documentation for %{name}
Requires:	%{name} = %{version}-%{release}
BuildArch:		noarch
%description doc
Documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gem_name}-%{version} -b1
%patch -P0 -p1
mv ../%{gem_name}-%{version}.gemspec .

%build

gem build ./%{gem_name}-%{version}.gemspec
%gem_install
%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
	%{buildroot}%{gem_dir}/
pushd %{buildroot}%{gem_instdir}
rm -rf .yardopts* \
	%{nil}
popd
mkdir -p %{buildroot}%{_bindir}
cp -a .%{_bindir}/* \
	%{buildroot}%{_bindir}/
find %{buildroot}%{gem_instdir}/bin -type f | xargs chmod 0755
rm -f %{buildroot}%{gem_cache}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

sed -i spec/cli/diff_spec.rb \
	-e '\@"searches for .gem file"@s|\([ \t]it \)|\txit |'
rspec -r spec_helper spec
%files -f %{oreon_filedir}/main.list
%files -n rubygem-yard-doc -f %{oreon_filedir}/rubygem-yard-doc.list

%changelog

%autochangelog
