# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/bussproofs
# catalog-date 2007-03-05 14:17:42 +0100
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-bussproofs
Version:	1.0
Release:	1
Summary:	Proof trees in the style of the sequent calculus
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bussproofs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bussproofs.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The package allows the construction of proof trees in the style
of the sequent calculus and many other proof systems. One novel
feature of the macros is they support the horizontal alignment
according to some centre point specified with the command
\fCenter. This is the style often used in sequent calculus
proofs. The package works in a Plain TeX document, as well as
in LaTeX; an exposition of the commands available is given in
the package file itself.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/bussproofs/bussproofs.sty
%doc %{_texmfdistdir}/doc/latex/bussproofs/testbp2.pdf
%doc %{_texmfdistdir}/doc/latex/bussproofs/testbp2.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
