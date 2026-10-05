%global source0_hash f5a6c56c1575bf9f51313d89b3e2901a7be0dd3073ac14792838952c58853ae4
%global source200_hash a5a3a1aec96113b1e953545c3d8c5117ff0220c56f7293c6fff7d35b1cd37c14
%global source201_hash da2739e6f56f89df300165e41facc375c0b03ca8ae68dcd2531afed409f0731e
%global source202_hash a8a5f228ffd13cadc03b5d08c7e51df9bd508dbbf06f783b327f3819246019b4
%global source203_hash 5194dad25d878985646a49df71bd985e8d2dd4c6b6765717093ac8a31bdb32e4
%global source205_hash 2daf3b4360ba9e07344210ccf29b6be9703d0abc66de4121f65d90119fe996ca
%global source207_hash 5e81d93a48869c58631bd967818cb530afd345137fc5e079f8a14914c41a8bbf
%global source209_hash 59994a1c33adf4e95c4557283238d91233d0b771027938e376c897270d900af0
%global source300_hash ebfffb41861ab1ccc989de2c9c2d11924e5ddded2728b053f5f2fddc8409c0e1
%global source301_hash a9d6347da0329bf118e9878617e50b5537eb9ec3c5fcd08852650713832d1ac1
%global source302_hash 051fc65d97c15e7cd646831368af8afec590b008c804d293aff114c74a1e2530
%global source303_hash 44cd3fdee9283d7b2e6a0990e518fe1e55df911879b04a3fc6bba1e86f14fc19
%global source304_hash 10f7e85b5ce53014c946b14c750b09097bed1892ecaf2cea05d12aab6e8677d2
%global source400_hash 1e16275273bc5bbee2a248f563f977d4177203a1624a7992cb842af0d800078b
%global source500_hash a9000043610a3e90c852e779a6b1a8eb724a9f312cf5f7ddd57862b010c65dc8

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q install --assumeno '" .. dep .. "' 2>&1")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    if string.find(out, "nothing provides", 1, true) then return true end
    if string.find(out, "No match", 1, true) then return true end
    if string.find(out, "Failed to resolve", 1, true) then return true end
    if string.find(out, "Nothing to do", 1, true) then return false end
    if string.find(out, "Operation aborted", 1, true) then return false end
    if string.find(out, "already installed", 1, true) then return false end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.byte(s, 1) == 37 and string.byte(s, 2) == 105 and string.byte(s, 3) == 102 and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.byte(s, 1) == 37 and string.byte(s, 2) == 105 and string.byte(s, 3) == 102 then
          depth = depth + 1
        elseif string.byte(s, 1) == 37 and string.byte(s, 2) == 101 and string.byte(s, 3) == 110 and string.byte(s, 4) == 100 and string.byte(s, 5) == 105 and string.byte(s, 6) == 102 then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.byte(s, 1) == 37 and string.byte(s, 2) == 101 and string.byte(s, 3) == 108 and string.byte(s, 4) == 115 and string.byte(s, 5) == 101 then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.byte(dep, 1) ~= 37 and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap
# Component versions, taken from gradle.properties
%global platform_version %{version}
%global jupiter_version %{version}
%global vintage_version %{version}

Name:           junit5
Version:        6.1.3
Release:        %autorelease
Summary:        Java regression testing framework
License:        EPL-2.0
URL:            https://junit.org/junit5/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/junit-team/junit5/archive/r%{version}/junit5-%{version}.tar.gz
# Aggregator POM (used for packaging only)
Source100:      aggregator.pom
# Platform POMs
Source200:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-commons/%{platform_version}/junit-platform-commons-%{platform_version}.pom
Source201:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console/%{platform_version}/junit-platform-console-%{platform_version}.pom
Source202:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-console-standalone/%{platform_version}/junit-platform-console-standalone-%{platform_version}.pom
Source203:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-engine/%{platform_version}/junit-platform-engine-%{platform_version}.pom
Source205:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-launcher/%{platform_version}/junit-platform-launcher-%{platform_version}.pom
Source207:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-suite-api/%{platform_version}/junit-platform-suite-api-%{platform_version}.pom
Source209:      https://repo1.maven.org/maven2/org/junit/platform/junit-platform-testkit/%{platform_version}/junit-platform-testkit-%{platform_version}.pom
# Jupiter POMs
Source300:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter/%{jupiter_version}/junit-jupiter-%{jupiter_version}.pom
Source301:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-api/%{jupiter_version}/junit-jupiter-api-%{jupiter_version}.pom
Source302:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-engine/%{jupiter_version}/junit-jupiter-engine-%{jupiter_version}.pom
Source303:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-migrationsupport/%{jupiter_version}/junit-jupiter-migrationsupport-%{jupiter_version}.pom
Source304:      https://repo1.maven.org/maven2/org/junit/jupiter/junit-jupiter-params/%{jupiter_version}/junit-jupiter-params-%{jupiter_version}.pom
# Vintage POM
Source400:      https://repo1.maven.org/maven2/org/junit/vintage/junit-vintage-engine/%{vintage_version}/junit-vintage-engine-%{vintage_version}.pom
# BOM POM
Source500:      https://repo1.maven.org/maven2/org/junit/junit-bom/%{version}/junit-bom-%{version}.pom

Patch:          0001-Drop-transitive-requirement-on-apiguardian.patch
Patch:          0002-Add-missing-module-static-requires.patch
Patch:          0003-Remove-legacy-XML-console-support.patch
Patch:          0004-Add-JRE-class-generated-from-template.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(de.siegmar:fastcsv)
BuildRequires:  mvn(info.picocli:picocli)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.opentest4j:opentest4j)
BuildRequires:  mvn(org.jspecify:jspecify)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-guide < 5.10.2-16
Obsoletes:      %{name}-javadoc < 5.10.2-16

%description
JUnit is a popular regression testing framework for Java platform.

%package        platform-console
Summary:        Console launcher for junit5
Requires:       junit5 = %{version}-%{release}
Requires:       %{name}-platform-console-jdk-binding
Suggests:       %{name}-platform-console-openjdk25 = %{version}-%{release}
%description    platform-console
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source200_hash}" = "none" || { f="%{SOURCE200}"; test -f "$f" || { echo "oreon: missing Source200 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source200_hash}" || { echo "oreon: Source200 hash mismatch" >&2; exit 1; }; }
test "%{source201_hash}" = "none" || { f="%{SOURCE201}"; test -f "$f" || { echo "oreon: missing Source201 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source201_hash}" || { echo "oreon: Source201 hash mismatch" >&2; exit 1; }; }
test "%{source202_hash}" = "none" || { f="%{SOURCE202}"; test -f "$f" || { echo "oreon: missing Source202 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source202_hash}" || { echo "oreon: Source202 hash mismatch" >&2; exit 1; }; }
test "%{source203_hash}" = "none" || { f="%{SOURCE203}"; test -f "$f" || { echo "oreon: missing Source203 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source203_hash}" || { echo "oreon: Source203 hash mismatch" >&2; exit 1; }; }
test "%{source205_hash}" = "none" || { f="%{SOURCE205}"; test -f "$f" || { echo "oreon: missing Source205 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source205_hash}" || { echo "oreon: Source205 hash mismatch" >&2; exit 1; }; }
test "%{source207_hash}" = "none" || { f="%{SOURCE207}"; test -f "$f" || { echo "oreon: missing Source207 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source207_hash}" || { echo "oreon: Source207 hash mismatch" >&2; exit 1; }; }
test "%{source209_hash}" = "none" || { f="%{SOURCE209}"; test -f "$f" || { echo "oreon: missing Source209 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source209_hash}" || { echo "oreon: Source209 hash mismatch" >&2; exit 1; }; }
test "%{source300_hash}" = "none" || { f="%{SOURCE300}"; test -f "$f" || { echo "oreon: missing Source300 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source300_hash}" || { echo "oreon: Source300 hash mismatch" >&2; exit 1; }; }
test "%{source301_hash}" = "none" || { f="%{SOURCE301}"; test -f "$f" || { echo "oreon: missing Source301 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source301_hash}" || { echo "oreon: Source301 hash mismatch" >&2; exit 1; }; }
test "%{source302_hash}" = "none" || { f="%{SOURCE302}"; test -f "$f" || { echo "oreon: missing Source302 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source302_hash}" || { echo "oreon: Source302 hash mismatch" >&2; exit 1; }; }
test "%{source303_hash}" = "none" || { f="%{SOURCE303}"; test -f "$f" || { echo "oreon: missing Source303 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source303_hash}" || { echo "oreon: Source303 hash mismatch" >&2; exit 1; }; }
test "%{source304_hash}" = "none" || { f="%{SOURCE304}"; test -f "$f" || { echo "oreon: missing Source304 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source304_hash}" || { echo "oreon: Source304 hash mismatch" >&2; exit 1; }; }
test "%{source400_hash}" = "none" || { f="%{SOURCE400}"; test -f "$f" || { echo "oreon: missing Source400 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source400_hash}" || { echo "oreon: Source400 hash mismatch" >&2; exit 1; }; }
test "%{source500_hash}" = "none" || { f="%{SOURCE500}"; test -f "$f" || { echo "oreon: missing Source500 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source500_hash}" || { echo "oreon: Source500 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n junit-framework-r%{version}
find -name '*.jar' -delete

cp -p %{SOURCE100} pom.xml

for source in $(echo %{sources} | cut -d ' ' -f3-); do
  module=${source}
  module=${module##*/}
  module=${module%%-*}
  if [ -d ${module}/src/module ]; then
    mkdir -p ${module}/src/main/java
    mv -t ${module}/src/main/java ${module}/src/module/*/module-info.java
  fi
  cp -p ${source} ${module}/pom.xml
  %pom_add_parent org.fedoraproject.xmvn.junit5:aggregator:any ${module}
  # OSGi BSN
  bsn=org.${module//-/.}
  %pom_xpath_inject pom:project "<properties><osgi.bsn>${bsn}</osgi.bsn></properties>" ${module}
  # Incorrect scope - API guardian is just annotation, needed only during compilation
  %pom_xpath_set -f "pom:dependency[pom:artifactId='apiguardian-api']/pom:scope" provided ${module}
  %pom_xpath_set -f "pom:dependency[pom:artifactId='jspecify']/pom:scope" provided ${module}
  %pom_xpath_set -f "pom:dependency[pom:scope='runtime']/pom:scope" compile ${module}
done

%pom_remove_parent junit-bom

# Add deps which are shaded by upstream and therefore not present in POMs.
%pom_add_dep org.junit.platform:junit-platform-commons:%{platform_version} junit-platform-console
%pom_add_dep org.junit.platform:junit-platform-launcher:%{platform_version} junit-platform-console
%pom_add_dep info.picocli:picocli junit-platform-console
%pom_add_dep de.siegmar:fastcsv junit-jupiter-params

%pom_disable_module junit-platform-console-standalone
%pom_remove_dep org.junit.platform:junit-platform-reporting junit-platform-console

%mvn_package :aggregator __noinstall

%build
%mvn_build -j -f

%install
%mvn_install

%jpackage_script org.junit.platform.console.ConsoleLauncher "" "" junit5:opentest4j:picocli:junit:hamcrest:fastcsv junit-platform-console

# JDK bindings
install -d -m 755 %{buildroot}%{_javaconfdir}/
ln -s %{_jpbindingdir}/%{name}-platform-console.conf %{buildroot}%{_javaconfdir}/%{name}-platform-console.conf
#
echo 'JAVA_HOME=%{_jvmdir}/jre-25-openjdk' > %{buildroot}%{_javaconfdir}/%{name}-platform-console-openjdk25.conf
%jp_binding --verbose --variant platform-console-openjdk25 --ghost %{name}-platform-console.conf --target %{_javaconfdir}/%{name}-platform-console-openjdk25.conf --provides %{name}-platform-console-jdk-binding --requires %{name}-platform-console --requires java-25-openjdk-headless
#
touch %{buildroot}%{_javaconfdir}/%{name}-platform-console-unbound.conf
%jp_binding --verbose --variant platform-console-unbound --ghost %{name}-platform-console.conf --target %{_javaconfdir}/%{name}-platform-console-unbound.conf --provides %{name}-platform-console-jdk-binding --requires %{name}-platform-console
#

%files -f .mfiles
%license LICENSE.md NOTICE.md

%files platform-console
%{_bindir}/junit-platform-console
%config %{_javaconfdir}/%{name}*.conf
%license LICENSE.md NOTICE.md

%changelog
%autochangelog
